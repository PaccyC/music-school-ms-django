
import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin


class AutoLogout(MiddlewareMixin):
    def process_request(self,request):
        if not request.user.is_authenticated:
            return
        
        current_time= datetime.datetime.now()
        last_activity= request.session.get('last_activity')
        
        if not last_activity:
            request.session['last_activity'] = current_time.isoformat()
            return
        
        elapsed_time=(current_time - datetime.datetime.fromisoformat(last_activity)).total_seconds()
        session_timeout=settings.SESSION_COOKIE_AGE
        
        if elapsed_time > session_timeout:
            logout(request)
            
        else:
            request.session['last_activity'] = current_time.isoformat()     
            