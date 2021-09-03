from .models import Subcategory, Category, Partner

def globalinfo(request):
    mcats = Category.objects.all()
    scats = Subcategory.objects.all()
    partners = Partner.objects.all()

    return {
        'mcats':mcats,
        'scats':scats,
        'partners':partners
    }

