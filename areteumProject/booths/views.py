from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet 
from .models import *
from .serializers import *


# 부스 소개 - 10/1 화
class BoothDay1ListView(APIView):
    def get(self, request):
        booths = Booth.objects.filter(Q(date='day1') | Q(date='both'))
        
        # 카테고리 선택됐을 시 
        selected_category = request.GET.get('category', None)
        if selected_category is not None:
            booths = booths.filter(category=selected_category)

        booths_count = booths.count()
        booths_list = Day1BoothSerializer(booths, many=True, context={'request':request})

        return Response({
            'booths_count':booths_count,
            'booths_list':booths_list.data,
        }, status=status.HTTP_200_OK)


# 부스 소개 - 10/2 수
class BoothDay2ListView(APIView):
    def get(self, request):
        booths = Booth.objects.filter(Q(date='day2') | Q(date='both'))
        
        # 카테고리 선택됐을 시 
        selected_category = request.GET.get('category', None)
        if selected_category is not None:
            booths = booths.filter(category=selected_category)

        booths_count = booths.count()
        booths_list = Day2BoothSerializer(booths, many=True, context={'request':request})

        return Response({
            'booths_count':booths_count,
            'booths_list':booths_list.data,
        }, status=status.HTTP_200_OK)


# 부스 소개 / 부스 알아보기 
class BoothDetailView(APIView):
    def get(self, request, booth_id):
        booth = Booth.objects.get(id=booth_id)
        booth_data = BoothSerializer(booth, context={'request':request}).data

        menu_groups = MenuGroup.objects.filter(booth=booth_id)

        food_list = []
        for menu_group in menu_groups:
            foods = Food.objects.filter(menu_group=menu_group)

            food_data = [
                    {
                        "name": food.name,
                        "price": food.price,
                    }
                    for food in foods
                ]
            food_list.append({
                "menu_group": menu_group.name,
                "menu_group_price": menu_group.price,
                "food_list": food_data,
            })

        # 주점일 경우 메뉴 노출
        if booth.category == '주점':
            return Response({
                'booth': booth_data, 
                'menu': food_list,
            }, status=status.HTTP_200_OK)
        
        return Response(booth_data, status=status.HTTP_200_OK)
    
# 부스 검색   
class SearchBoothView(generics.ListAPIView):
    serializer_class = SearchBoothSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Booth.objects.all()
        search_term = self.request.query_params.get('search', None)
        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'count': queryset.count(),
            'results': serializer.data
        }, status=status.HTTP_200_OK)
    
# 솜톡
class SomTalkViewSet(ModelViewSet):
    queryset = SomTalk.objects.all()
    serializer_class = SomTalkSerializer