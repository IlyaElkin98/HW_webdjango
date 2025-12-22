from django.forms import forms, ModelForm
from product.models import Product


class ProductForm(ModelForm):
    ignore_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]
    class Meta:
        model = Product
        fields = ["name", "description", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "class" : "form-control",
            "placeholder" : "Введите наименование товара. Кроме слов исключений"
        })

        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите Описание"
        })

        self.fields["price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите цену товара"
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        self.validate_ignore_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        self.validate_ignore_words(description)
        return description

    def validate_ignore_words(self, text):
        if text:
            for word in self.ignore_words:
                if word.lower() in text.lower():
                    raise forms.ValidationError(f"Слово '{word}' запрещено. Пожалуйста, измените текст.")


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной. Пожалуйста, введите корректное значение.")
        return price


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ["publication_status"]

