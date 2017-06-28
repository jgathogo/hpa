from django.db import models

class Product(models.Model):
	item = models.CharField(max_length=200)
	unit = models.CharField(max_length=50)
	no_of_pieces = models.IntegerField()

	def __str__(self):
		return self.item

	class Meta:
		ordering = ('item',)

class Country(models.Model):
	country = models.CharField(max_length=20)

	def __str__(self):
		return self.country

	class Meta:
		ordering = ('country',)


class Town(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	town = models.CharField(max_length=20)

	def __str__(self):
		return self.town

	class Meta:
		ordering = ('town',)

class StockCard(models.Model):
	STOCKMOVEMENT = (
        ('IN', 'Stock coming in'),
        ('OUT', 'Stock going out'),
        
    )

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	transaction_date = models.DateField()
	stock_in_or_out = models.CharField(max_length=3, choices=STOCKMOVEMENT)
	supplier = models.CharField(max_length=20, blank=True)
	to_where = models.ForeignKey(Town, on_delete=models.CASCADE, blank=True, null=True)
	document_no = models.CharField(max_length=50)
	stock_amount = models.FloatField()

	def __str__(self):
		return '%s %s %s %s %s' % (self.product, self.transaction_date, self.document_no, " : Stock Movement - ", self.stock_in_or_out)



	