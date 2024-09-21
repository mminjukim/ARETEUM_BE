from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, filters
from rest_framework.response import Response
from django.db.models import Q

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
        booth = BoothSerializer(booth, context={'request':request})
        return Response(booth.data, status=status.HTTP_200_OK)
    
# 부스 검색   
class SearchBoothView(generics.ListAPIView):
    queryset = Booth.objects.all()
    serializer_class = SearchBoothSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']