from .models import (UserProfile, Category, SubCategory,
                     Product, Review,
                     Cart, CartItem)
from .serilizers import (UserProfileSerializers, CategoryListSerializers,
                          SubCategoryListSerializers, SubCategoryDetailSerializers, ProductListSerializers,
                          ProductDetailSerializers, CategoryDetailSerializers,
                          ReviewSerializers,CartSerializers, CartItemSerializers)
from rest_framework import viewsets, generics, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import ProductPagination, CategoryPagination


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
    pagination_class = CategoryPagination


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializers


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializers


class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryDetailSerializers



class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['article_number']
    ordering_fields = ['price', 'created_date']
    pagination_class = ProductPagination


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializers


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers