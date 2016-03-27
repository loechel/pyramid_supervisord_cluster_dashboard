from pyramid.view import view_config
from .models import BaseModel


@view_config(context=BaseModel, renderer='templates/main_template.pt')
def my_view(request):
    return {'project': 'pyramid_supervisord_cluster_dashboard'}
