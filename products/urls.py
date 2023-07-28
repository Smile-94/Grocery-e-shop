from django.urls import path


app_name = 'products'

# Import Views
from products.views import manage_category
from products.views import manage_subCategory
from products.views import manage_product


# Manage Product Category
urlpatterns = [
    path('add-category/', manage_category.AddCategoryView.as_view(), name='add_category'),
    path('update-category/<int:pk>/', manage_category.UpdateProductsCategoryView.as_view(), name='update_category'),
    path('delete-category/<int:pk>/', manage_category.DeleteCategoryView.as_view(), name='delete_category'),
]

# Manage Product Sub Category
urlpatterns += [
   path('add-subCategory/', manage_subCategory.AddSubCategoryView.as_view(), name='add_subCategory'), 
   path('update-subCategory/<int:pk>/', manage_subCategory.UpdateProductsSubCategoryView.as_view(), name='update_subCategory'), 
   path('delete-subCategory/<int:pk>/', manage_subCategory.DeleteSubCategoryView.as_view(), name='delete_subCategory'), 
]

# Manage Product
urlpatterns +=[
    path('product-list/', manage_product.ProductListView.as_view(), name='product_list' ),
    path('add-product/', manage_product.AddProductView.as_view(), name='add_product' ),
]



