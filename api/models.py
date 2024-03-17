
from django.db import models
from django.contrib.auth.models import User

class TypeCar(models.Model):
    code = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class City(models.Model):
    name = models.CharField(max_length=100)
    localisation = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    is_airport = models.BooleanField(default=False)
    destination_city = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    description_city = models.TextField(null=True, blank=True)
    picture_city = models.URLField(null=True, blank=True)
    gallerie_city = models.JSONField(default=list)

    def __str__(self):
        return self.name
    


class Partenaire(models.Model):
    name_partner_company = models.CharField(max_length=100)
    code_partner_company = models.CharField(max_length=100)
    email_partner_company = models.EmailField()
    phone_number_partner_company = models.CharField(max_length=100)
    address_partner_company = models.CharField(max_length=255)
    localisation_partner_company = models.CharField(max_length=100, null=True, blank=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name_partner_company




class Car(models.Model):
    code = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    air_conditioner = models.BooleanField(default=True)
    name_model = models.CharField(max_length=100)
    name_mark = models.CharField(max_length=100)
    picture = models.URLField()
    status = models.CharField(max_length=100)
    year = models.CharField(max_length=100, null=True, blank=True)
    fuel = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    gallerie = models.JSONField(default=list)
    portes = models.IntegerField()
    type = models.ForeignKey(TypeCar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_mark} {self.name_model}"


class NavetteAeroport(models.Model):
    code = models.CharField(max_length=100)
    price_airport = models.DecimalField(max_digits=10, decimal_places=2)
    price_airport_roundTrip = models.DecimalField(max_digits=10, decimal_places=2)
    number_pax_airport = models.CharField(max_length=100)
    number_luggage_airport = models.CharField(max_length=100)
    chaise_bebe = models.DecimalField(max_digits=10, decimal_places=2)
    animal_compagnie = models.DecimalField(max_digits=10, decimal_places=2)
    adress_supplementaire = models.DecimalField(max_digits=10, decimal_places=2)
    is_entreprise = models.BooleanField(default=False)
    enable = models.BooleanField(default=True)
    from_city = models.ForeignKey(City, related_name='from_city', on_delete=models.CASCADE)
    to_city = models.ForeignKey(City, related_name='to_city', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
class OutsideRental(models.Model):
    code = models.CharField(max_length=100)
    package_one_way = models.DecimalField(max_digits=10, decimal_places=2)
    is_entreprise = models.BooleanField(default=False)
    chaise_bebe = models.DecimalField(max_digits=10, decimal_places=2)
    animal_compagnie = models.DecimalField(max_digits=10, decimal_places=2)
    adress_supplementaire = models.DecimalField(max_digits=10, decimal_places=2)
    number_pax = models.CharField(max_length=100)
    number_luggage = models.CharField(max_length=100)
    from_city = models.ForeignKey(City, related_name='package_from_city', on_delete=models.CASCADE)
    to_city = models.ForeignKey(City, related_name='package_to_city', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Circuit(models.Model):
    code = models.CharField(max_length=100)
    enable = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    medias_images = models.JSONField()
    medias_video = models.URLField(max_length=500, blank=True)
    serice_include = models.JSONField()
    serice_exclus = models.JSONField()
    type_coverture = models.JSONField()
    disponibility = models.JSONField()
    cities = models.ManyToManyField(City)
    partner = models.ForeignKey(Partenaire, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='circuit_created_by', null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='circuit_updated_by', null=True, blank=True)
    disable_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='circuit_disable_by', null=True, blank=True)

    def __str__(self):
        return self.title

class Rentalcar(models.Model):
    code = models.CharField(max_length=100)
    price_rental = models.DecimalField(max_digits=10, decimal_places=2)
    price_with_driver = models.DecimalField(max_digits=10, decimal_places=2)
    with_driver = models.CharField(max_length=100)
    price_repas_driver = models.DecimalField(max_digits=10, decimal_places=2)
    price_hebergement_driver = models.DecimalField(max_digits=10, decimal_places=2)
    price_chaise_bebe = models.DecimalField(max_digits=10, decimal_places=2)
    reduction_pourcentage = models.IntegerField()
    reduction_days = models.IntegerField()
    limit_km = models.IntegerField()
    price_extra_km = models.DecimalField(max_digits=10, decimal_places=2)
    cities = models.ManyToManyField(City, related_name='location_cities')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_location')
    partner = models.ForeignKey('Partenaire', on_delete=models.CASCADE, related_name='partner_location')
    number_place = models.IntegerField()
    caution = models.DecimalField(max_digits=10, decimal_places=2)
    with_reduction = models.BooleanField()

    def __str__(self):
        return self.code
