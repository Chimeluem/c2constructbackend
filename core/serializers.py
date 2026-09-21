from rest_framework import serializers
from .models import Contact, Job, Qualifications, SiteDetail


class SiteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteDetail
        fields = ['phone','address']

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['first_name','email', 'last_name', 'phone', 'info']

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualifications
        fields = ['first_aider', 'cscs_card', 'Fire_Marshall', 'driving_license'
                  ]

class JobSerializer(serializers.ModelSerializer):
    qualifications = QualificationSerializer()
    class Meta:
        model = Job
        fields = ['firstName', 'email', 'lastName', 'phoneNumber', 'licenseType', 'qualifications',
                  'state', 'city', 'country', 'address1', 'address2', 'zipCode', 'additionalInfo'
                  ]


    def create(self, validated_data):
        qualifications = validated_data.pop('qualifications')
        if qualifications :
            if qualifications['first_aider'] == 'False':
                qualifications['first_aider'] = False
            else:
                qualifications['first_aider'] = True

            if qualifications['cscs_card'] == 'False':
                qualifications['cscs_card'] = False
            else:
                qualifications['cscs_card'] = True

            if qualifications['Fire_Marshall'] == 'False':
                qualifications['Fire_Marshall'] = False
            else:
                qualifications['Fire_Marshall'] = True

            if qualifications['driving_license'] == 'False':
                qualifications['driving_license'] = False
            else:
                qualifications['driving_license'] = True
            job = Job.objects.create(
                firstName=validated_data.get('firstName'),
                email=validated_data.get('email'),
                lastName=validated_data.get('lastName'),
                phoneNumber=validated_data.get('phoneNumber'),
                licenseType=validated_data.get('licenseType'),
                state=validated_data.get('state'),
                city=validated_data.get('city'),
                country=validated_data.get('country'),
                address1=validated_data.get('address1'),
                address2=validated_data.get('address2'),
                zipCode=validated_data.get('zipCode'),
                additionalInfo=validated_data.get('additionalInfo'),
                first_aider=qualifications['first_aider'],
                cscs_card=bool(qualifications['cscs_card']),
                Fire_Marshall=bool(qualifications['Fire_Marshall']),
                driving_license=bool(qualifications['driving_license'])

            )
            return job
        raise serializers.ValidationError("your application was successful")





