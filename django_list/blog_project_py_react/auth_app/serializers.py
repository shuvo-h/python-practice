from rest_framework import serializers
from users.models import User
from django.utils import timezone

"""
    Add as many validate_<fieldname> methods as needed for field-specific validation.
    Use the validate() method to validate multiple fields together.
"""
class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username', 'full_name', 'password', 'role', 'phone_number']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'phone_number': {
                'required': True,
            },
            'full_name': {
                'required': True,
            },
        }

     # Ensure email is unique
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    # Ensure username is unique
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    # Example: Validate phone_number to ensure it's in a specific format or not blank
    def validate_phone_number(self, value):
        if not value:
            raise serializers.ValidationError("Phone number cannot be blank.")
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be 10 digits.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one number.")
        return value


    # This method validates multiple fields together, if necessary
    def validate(self, data):
        # Example: Ensure that email and username are not the same
        if data['email'] == data['username']:
            raise serializers.ValidationError("Email and username cannot be the same.")

        # Add any other cross-field validation logic here
        return data

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.generate_otp()
        # Send OTP to email
        # user.send_otp_email()  # Implement this method to send email
        user.save()
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'email', 'username', 'full_name', 'role', 'verified', 'phone_number']

class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'], otp=data['otp'])
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid OTP or email.')

        if user.otp_expiration < timezone.now():
            raise serializers.ValidationError('OTP has expired.')

        return data

    def save(self, **kwargs):
        user = User.objects.get(email=self.validated_data['email'])
        user.verified = True
        user.otp = None  # Clear OTP after verification
        user.otp_expiration = None
        user.save()
        return user


