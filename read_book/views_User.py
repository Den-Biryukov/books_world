from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from read_book.pagination import ListPagination
from read_book.permissions import IsStaff
from read_book.serializer_Likes import LikeFullNameOfBookSerializer
from read_book.serializer_Rating import RatingFullNameOfBookSerializer
from read_book.serializer_User import UserDetailSerializer, UserSerializer


class AllUsersForStaffListAPIView(generics.ListAPIView):
    """List full information of users for staff"""

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsStaff, )
    pagination_class = ListPagination


class UserDetailForStaffListAPIView(generics.ListAPIView):
    """List full information of user for staff"""

    permission_classes = (IsStaff, )

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        return Response({'user': UserDetailSerializer(user).data})


class UserListAPIView(generics.ListAPIView):
    """List information of users"""

    queryset = User.objects.all()
    pagination_class = ListPagination
    serializer_class = UserSerializer


class UserDetailListAPIView(generics.ListAPIView):
    """List information of user"""

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        return Response({'user': UserSerializer(user).data})


class UserDetailLikesAPIView(generics.ListAPIView):
    """display user likes for books"""

    def get(self, request, pk):
        user_likes_all = User.objects.get(id=pk).likes.all()
        user = User.objects.get(id=pk)
        return Response({f'{user}': LikeFullNameOfBookSerializer(user_likes_all, many=True).data})


class UserDetailRatingAPIView(generics.ListAPIView):
    """display user rating for books"""

    def get(self, request, pk):
        user_rating_all = User.objects.get(id=pk).rating.all()
        user = User.objects.get(id=pk)
        return Response({f'{user}': RatingFullNameOfBookSerializer(user_rating_all, many=True).data})
