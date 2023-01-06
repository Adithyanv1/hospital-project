from django import forms

from.models import booking
class DateInput(forms.DateInput):
    input_type='date'
class BookingForm(forms.ModelForm):
    class Meta:
        model=booking
        fields="__all__"
        widgets={
            'booking_date':DateInput(),
        }
        abels={
            'p_name':"Patient Name :",
            'p_phone':"Patient Contact number :",
            'p_email':"patient Email:",
            'doc_name':"Doctor name:",
            'booking_date':"Booking Date :",
            

        }