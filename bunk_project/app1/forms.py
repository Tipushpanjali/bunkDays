from django import forms
    
class bunk_form(forms.Form):
    totalDays = forms.IntegerField(label="Total Days")
    totalAttendanceNeeded= forms.IntegerField(label="Total attendance needed(in %)")
    PresentAttendance = forms.IntegerField(label="present attendance(in %)")
    DaysGone= forms.IntegerField(label="days passed?")
