from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

STATUS = (('1', '新品未使用'), ('2', '未使用に近い'), ('3', '目立った傷や汚れなし'), ('4', '全体的に状態が悪い'))
SHIPPING_BURDEN = (('1', '送料込み（出品者負担）'), ('2', '着払い（購入者負担）'), ('3', '未定'), ('4', '7日以内'), ('5', '未定'))
SHIPPING_DAYS = (('1', '即日'), ('2', '２〜３日以内'), ('3', '5日以内'), ('4', '7日以内'), ('5', '未定'))


class ItemModel(models.Model):
    name = models.CharField(verbose_name='商品名', max_length=30)
    price = models.IntegerField(verbose_name='価格', validators=[MinValueValidator(100),
                                                               MaxValueValidator(9999999)])
    memo = models.TextField(verbose_name='商品説明')
    status = models.CharField(
        verbose_name='商品状態',
        max_length=100,
        choices=STATUS
    )
    shipping_burden = models.CharField(
        verbose_name='発送料の負担',
        max_length=100,
        choices=SHIPPING_BURDEN
    )
    shipping_area = models.CharField(verbose_name='発送地域', max_length=10)

    shipping_days = models.CharField(
        verbose_name='発送までの日数',
        max_length=100,
        choices=SHIPPING_DAYS
    )

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    itemmodel = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    src = models.ImageField(verbose_name='出品画像')
