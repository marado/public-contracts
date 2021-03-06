from sphinxql import indexes, fields
from .models import Entity, Contract


class EntityIndex(indexes.Index):
    name = fields.Text('name')

    class Meta:
        model = Entity


class ContractIndex(indexes.Index):
    name = fields.Text('description')
    description = fields.Text('contract_description')

    signing_date = fields.Date('signing_date')

    category_id = fields.Integer('category')

    class Meta:
        model = Contract
