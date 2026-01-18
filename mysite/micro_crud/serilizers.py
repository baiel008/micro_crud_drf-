from .models import *
from rest_framework import serializers

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_image', 'category_name']



class SubCategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name']


class CategoryDetailSerializers(serializers.ModelSerializer):
    category_sub = SubCategoryListSerializers(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'category_sub']


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']



class ProductListSerializers(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y')
    product_images = ProductImageSerializers(read_only=True, many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_images', 'price', "product_type",
                  'get_avg_rating', 'get_count_people', 'created_date']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


class SubCategoryDetailSerializers(serializers.ModelSerializer):
    products = ProductListSerializers(read_only=True, many=True)

    class Meta:
        model = SubCategory
        fields = ['sub_category_name', 'products']


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductDetailSerializers(serializers.ModelSerializer):
    created_date = serializers.DateField(format='%d-%m-%Y')
    product_images = ProductImageSerializers(read_only=True, many=True)
    subcategory = SubCategoryListSerializers()
    product_reviews = ReviewSerializers(read_only=True, many=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product_name', 'subcategory', 'price', 'article_number', "product_type",
                  'video', 'product_images', 'description', 'created_date',
                  'get_avg_rating', 'get_count_people', 'product_reviews']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()


