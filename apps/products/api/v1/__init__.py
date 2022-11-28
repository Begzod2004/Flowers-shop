# @api_view(['GET'])
# def Product_api_view(request, pk=0):
#     if request.method == 'GET':
#         if pk == 0:
#             return Response(data=ProductSerializer(instance=Product.objects.all(), many=True).data, status=200)
#         else:
#             the_Product = get_object_or_404(Product, pk=pk)
#             return Response(data=ProductSerializer(instance=the_Product).data, status=200)
   
    
# class ProductListAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductReviewaSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')


# class ProductCreateAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     parser_classes = (FormParser, MultiPartParser)
