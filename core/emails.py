from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.conf import settings


def send_otp_via_email(email):
    subject = "Contact Confirmation"
    html_content = render_to_string("contact.html", {"email": email})
    mail = EmailMessage(
        subject,
        html_content,
        settings.EMAIL_HOST_USER,
        to=[email, 'c2constructionsec@hotmail.com']
    )
    mail.content_subtype = "html"
    mail.fail_silently = False
    mail.send()


def send_contact_via_emailtoadmin(contact):
    subject = "New Contact Message"
    html_content = render_to_string("contactadmin.html", {
        "email": contact.email,
        "first_name": contact.first_name,
        "last_name": contact.last_name,
        "phone": contact.phone,
        "info": contact.info,
    })
    mail = EmailMessage(
        subject,
        html_content,
        settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER, 'c2constructionsec@hotmail.com']
    )
    mail.content_subtype = "html"
    mail.fail_silently = False
    mail.send()


def send_job_via_emailtoadmin(job):
    subject = "New Job Application"
    html_content = render_to_string("jobsadmin.html", {
        "email": job.email,
        "first_name": job.firstName,
        "last_name": job.lastName,
        "phone": job.phoneNumber,
        "license_type": job.licenseType,
        "state": job.state,
        "city": job.city,
        "country": job.country,
        "address1": job.address1,
        "address2": job.address2,
        "zip_code": job.zipCode,
        "additional_info": job.additionalInfo,
    })
    mail = EmailMessage(
        subject,
        html_content,
        settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER, 'c2constructionsec@hotmail.com']
    )
    mail.content_subtype = "html"
    mail.fail_silently = False
    mail.send()