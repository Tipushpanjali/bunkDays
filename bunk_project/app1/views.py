from django.shortcuts import render, redirect
from .forms import bunk_form
from .models import BunkEntry
def bunk_view(request):
    result = None 

    if request.method == 'POST':
        form = bunk_form(request.POST)
        if form.is_valid():
            total_days = form.cleaned_data['totalDays']
            attendance_needed = form.cleaned_data['totalAttendanceNeeded']
            present_attendance = form.cleaned_data['PresentAttendance']
            days_gone = form.cleaned_data['DaysGone']

            # Calculate current attendance %
            a=(attendance_needed*total_days)/100
            b=(present_attendance*days_gone)/100
#            actual_attendance_percent = (present_attendance / total_days) * 100

            # Calculate how many more days can be missed
 #           max_bunkable_days = (present_attendance * 100 / attendance_needed) - total_days
            remaining_days= a-b    
            DaysLeft=total_days-days_gone        
            if DaysLeft >= remaining_days:
                result = f"You are safe! You can still bunk around {DaysLeft-remaining_days} day(s)."
            elif remaining_days>=DaysLeft:
                result = f"Warning! You need to attend at least {DaysLeft+(remaining_days-DaysLeft)} more day(s) to meet attendance requirements."
            entry = BunkEntry()
            entry.totalDays = total_days
            entry.totalAttendanceNeeded = attendance_needed
            entry.presentAttendance = present_attendance
            entry.daysGone = days_gone
            entry.resultMessage = result
            entry.save()
            request.session['result'] = result
 # Temporarily store result
            return redirect('bunk') 
    else:
        form = bunk_form()
        result = request.session.pop('result', None)

    return render(request, 'index.html', {'form': form, 'result': result})
