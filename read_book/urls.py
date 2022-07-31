from django.urls import path
from read_book.views_Book import BookAPIView, BookRetrieveUpdateDestroyAPIView, BookListCreateAPIView, \
                                 BookListdetailUpdateAPIView, BookListdetailDeleteAPIVew

from read_book.views_comments import CommentListCreateView, CommentDeleteAPIView, CommentUpdateAPIView

# Book
urlpatterns = [
    # path('book/', BookAPIView.as_view()),
    path('book/', BookListCreateAPIView.as_view()),
    path('book/update/<int:pk>', BookListdetailUpdateAPIView.as_view()),
    path('book/delete/<int:pk>', BookListdetailDeleteAPIVew.as_view()),
    # path('book/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view()),
]

# Comment
urlpatterns += [
    path('comments/', CommentListCreateView.as_view()),
    path('comment_delete/<int:pk>', CommentDeleteAPIView.as_view()),
    path('comment_update/<int:pk>', CommentUpdateAPIView.as_view()),
]
