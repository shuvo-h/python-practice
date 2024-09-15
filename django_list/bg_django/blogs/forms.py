from django import forms

class BlogRegistration(forms.Form):
    blog_id = forms.CharField(
        max_length=10,
        required=True,
        label="Blog ID",
        label_suffix=": ",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Blog ID',
            'maxlength': 10
        }),
        help_text="Unique ID for the blog (max 10 characters)."
    )

    title = forms.CharField(
        max_length=100,
        required=True,
        label="Blog Title",
        label_suffix=": ",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Blog Title'
        }),
        help_text="Enter a descriptive title for your blog (max 100 characters)."
    )

    desc = forms.CharField(
        required=True,
        label="Description",
        label_suffix=": ",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Blog Description',
            'rows': 5
        }),
        help_text="Provide a detailed description of your blog."
    )

    name = forms.CharField(
        max_length=50,
        required=True,
        label="Author Name",
        label_suffix=": ",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        }),
        help_text="Your full name (max 50 characters)."
    )

    email = forms.EmailField(
        required=True,
        label="Email Address",
        label_suffix=": ",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        }),
        help_text="Provide a valid email address."
    )

    def clean_blog_id(self):
        blog_id = self.cleaned_data['blog_id']
        # You can add custom validation here
        if not blog_id.isalnum():
            raise forms.ValidationError("Blog ID should contain only alphanumeric characters.")
        return blog_id

    def clean_title(self):
        title = self.cleaned_data['title']
        # Custom title validation (if needed)
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
