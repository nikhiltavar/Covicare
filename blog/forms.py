from django.forms import ModelForm
from tinymce.widgets import TinyMCE
from .models import Blog 



class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' 