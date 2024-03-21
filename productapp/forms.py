from django import forms

from .models import Product,Category,Comment

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['image','name','category','price','description',]
        
        
        widgets= {
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commenter_name','comment_body',)
        widgets = {
            'commenter_name':forms.TextInput(attrs={'class':'form-control'}),
            'comment_body': forms.Textarea(attrs={'class':'form-control'}),  
        }