# -*- encoding:utf-8 -*-
__author__ = 'cysnake4713'

from openerp.osv import osv
from openerp.osv import fields
from openerp import SUPERUSER_ID
import openerp.tools as tools
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.tools.translate import _


#A use B

#TODO
def _function_field_funt_global(cr, table, ids, field_name, arg, context):
    pass


#TODO
def _function_field_fnct_inv_global(cr, table, ids, field_name, field_value, arg, context):
    pass


#TODO
def _function_field_fnct_search_global(cr, uid, obj, name, args, context):
    pass


class DemoA(osv.osv):
    # Examples:
    #    _inherits = {
    #       'tiny.object_a': 'object_a_id'(the column name used in this model stored foreign key),
    #       'tiny.object_b': 'object_b_id',
    #       ... ,
    #       'tiny.object_n': 'object_n_id'
    #    }
    # The object 'tiny.object' inherits from all the columns and all the methods from
    # the n objects 'tiny.object_a', ..., 'tiny.object_n'.
    _inherits = {}
    # The name of the osv object which the current object inherits from.
    # _name == _inherit means override old model
    # _name != _inherit means inherit in new new model
    _inherit = ''
    # Name of the field in which the name of every resource is stored.
    # Default value: 'name'. Note: by default, the name_get method simply returns the content of this field.
    _name = 'tr.demo.a'
    # Name of the field in which the name of every resource is stored. Default value: 'name'.
    # Note: by default, the name_get method simply returns the content of this field.
    _rec_name = 'char_field'
    #  TODO
    _constraints = ''
    #  TODO
    _sql_constraints = ''
    # Determines whether or not the write access to the resource must be logged.
    # If true, four fields will be created in the SQL table: create_uid, create_date, write_uid, write_date.
    # Those fields represent respectively the id of the user who created the record,
    # the creation date of record, the id of the user who last modified the record,
    # and the date of that last modification. This data may be obtained by using the perm_read method.
    _log_access = True
    # Name of the fields used to sort the results of the search and read methods.
    # Default value: 'id'.
    # Examples:
    #   _order = "name"
    #   _order = "date_order desc"
    _order = 'id'
    #Name of the SQL sequence that manages the ids for this object. Default value: None.
    _sequence = None
    #Determines whether a corresponding PostgreSQL table must be generated automatically from the object.
    #Setting _auto to False can be useful in case of OpenERP objects generated from PostgreSQL views.
    #See the "Reporting From PostgreSQL Views" section for more details.
    _auto = True
    # SQL code executed upon creation of the object (only if _auto is True).
    # It means this code gets executed after the table is created.
    _sql = ''
    # Name of the SQL table. Default value:
    # the value of the _name field above with the dots ( . ) replaced by underscores ( _ ).
    _table = 'tr_demo_a'

    # noinspection PyUnusedLocal
    def _get_selection(self, cursor, user_id, context=None):
        return (
            ('choice1', 'This is the choice 1'),
            ('choice2', 'This is the choice 2'))

    def _sel_func(self, cr, uid, context=None):
        obj = self.pool.get('tr.demo.b')
        ids = obj.search(cr, uid, [])
        res = obj.read(cr, uid, ids, ['name', 'id'], context)
        res = [(r['id'], r['name']) for r in res]
        return res

    # noinspection PyUnusedLocal
    def _function_field_funt_method(self, cr, uid, ids, field_name, arg, context):
        """
            Either way, it must return a dictionary of values of the form
            {'id_1_': 'value_1_', 'id_2_': 'value_2_',...}.

            If multi is set, then field_name is replaced by field_names:
            a list of the field names that should be calculated.
            Each value in the returned dictionary is also a dictionary from field name to value.
            For example, if the fields 'name', and 'age' are both based on the vital_statistics function,
            then the return value of vital_statistics might look like this when ids is [1, 2, 5]:
            {
                1: {'name': 'Bob', 'age': 23},
                2: {'name': 'Sally', 'age', 19},
                5: {'name': 'Ed', 'age': 62}
            }
        """
        result = dict.fromkeys(ids, False)
        for _ in self.browse(cr, uid, ids, context=context):
            pass
        return result

    #TODO
    def _function_field_fnct_inv_method(self, cr, uid, ids, field_name, field_value, arg, context):
        pass

    # noinspection PyUnusedLocal
    # TODO
    def _function_field_fnct_search_method(self, cr, uid, obj, name, args, context):
        """
            The return value is a list containing 3-part tuples which are used in search function:
            return [('id','in',[1,3,5])]
            obj is the same as self, and name receives the field name.
            args is a list of 3-part tuples containing search criteria for this field,
            although the search function may be called separately for each tuple.
        """
        return args

    def _function_field_store_method(self, cr, uid, ids, context=None):
        pass

    _columns = {
        'char_field': fields.char(
            # The field name as it should appear in a label or column header.
            # Strings containing non-ASCII characters must use python unicode objects.
            # For example: 'tested': fields.boolean(u'Testé')
            string='Name',
            # The size of the field in the database: number characters or digits.
            size=50,
            # True if this field must have a value before the object can be saved, otherwise False.
            required=True,
            # True if the user cannot edit this field, otherwise False.
            readonly=False,
            # Lets you override other parameters for specific states of this object.
            # Accepts a dictionary with the state names as keys and a list of name/value tuples as the values.
            # For example: states={'posted':[('readonly',True)]}
            states=None,
            # True if the content of this field should be translated, otherwise False.
            translate=False,
            # TODO:Whether or not the user can define default values on other fields depending on the value of this field.
            # Those default values need to be defined in the ir.values table.
            change_default=False,
            # A description of how the field should be used: longer and more descriptive than string.
            # It will appear in a tooltip when the mouse hovers over the field.
            help="",
            # Hide the field's value in forms. For example, a password.
            # TODO
            invisible=False,
            # Default value for the select attribute in the view. 1 means basic search, and 2 means advanced search.
            select=1,
        ),
        'boolean_field': fields.boolean(string='Boolean'),
        'integer_field': fields.integer(string='Integer'),
        'float_field': fields.float(
            string='Float',
            # The optional parameter digits defines the precision and scale of the number.
            # The scale being the number of digits after the decimal point whereas the precision is
            # the total number of significant digits in the number (before and after the decimal point).
            # If the parameter digits is not present, the number will be a double precision floating point number.
            # Warning: these floating-point numbers are inexact (not any value can be converted to its binary representation)
            # and this can lead to rounding errors. You should always use the digits parameter for monetary amounts.
            digits=(10, 2),
            # synopsis: digits_compute(cr) ->  (precision, scale)
            digits_compute=None,
            required=False,
        ),
        'text_field': fields.text('Text'),
        'date_field': fields.date('Date'),
        'datetime_field': fields.datetime('Datetime'),
        'binary_field': fields.binary('Binary'),
        'selection_simple_field': fields.selection(selection=[('yes', 'Yes'), ('no', 'No')], string='Selection Simple'),
        'selection_complex_field': fields.selection(_get_selection, 'Selection Complex'),
        'many2one_field': fields.many2one(
            obj='tr.demo.b',
            # What should happen when the resource this field points to is deleted.
            # Predefined value: "cascade", "set null", "restrict", "no action", "set default"
            # Default value: "set null"
            string='Many2one Field',
            # TODO
            auto_join=False,
            ondelete='set null',
            # Using relation fields many2one with selection.
            selection=_sel_func,
            # Domain restriction on a relational field.
            # Example: domain=[('field','=',value)])
            domain=[],
            # Default value for the on_change attribute in the view.
            # This will launch a function on the server when the field changes in the client.
            # For example, on_change="onchange_shop_id(shop_id)".
            on_change=None,
        ),
        'related_field': fields.related(
            'many2one_field',
            'many2many_field',
            # type is the type of that desired field.
            type="many2many",
            # Use relation if the desired field is still some kind of reference. relation is the table to look up that reference in.
            relation="tr.demo.a",
            string="Related Field",
        ),
        #
        # Values: (0, 0,  { fields })    create
        #         (1, ID, { fields })    update (write fields to ID)
        #         (2, ID)                remove (calls unlink on ID, that will also delete the relationship because of the ondelete)
        #         (3, ID)                unlink (delete the relationship between the two objects but does not delete ID)
        #         (4, ID)                link (add a relationship)
        #         (5, ID)                unlink all
        #         (6, ?, ids)            set a list of links
        'one2many_field': fields.one2many(
            obj='tr.demo.b',
            fields_id='a_id',
            string='one2many Field',
            # TODO
            limit=None,
            # TODO
            auto_join=False,
            # TODO:
            # Define a variable's value visible in the view's context or an on-change function.
            # Used when searching child table of one2many relationship?
            context={},
            domain=[],
            #one2many can't be used as condition for defaults
            change_default=False,
        ),
        'many2many_field': fields.many2many(
            # destination model
            obj='tr.demo.b',
            # optional name of the intermediary relationship table. If not specified,
            # a canonical name will be derived based on the alphabetically-ordered
            # model names of the source and destination (in the form: ``amodel_bmodel_rel``).
            # Automatic naming is not possible when the source and destination are
            # the same, for obvious ambiguity reasons.
            rel='rel_tr_demo_a_b',
            # optional name for the column holding the foreign key to the current
            # model in the relationship table. If not specified, a canonical name
            # will be derived based on the model name (in the form: `src_model_id`).
            id1='a_id',
            # optional name for the column holding the foreign key to the destination
            # model in the relationship table. If not specified, a canonical name
            # will be derived based on the model name (in the form: `dest_model_id`)
            id2='b_id',
            string='Many2many Field B',
            # TODO
            limit=None,
        ),
        'function_field': fields.function(
            # fnct is the function or method that will compute the field value.
            # It must have been declared before declaring the functional field.
            # fnct = _function_field_fnct_inv_global,
            fnct=_function_field_funt_method,
            # fnct_inv is the function or method that will allow writing values in that field.
            # fnct_inv=_function_field_fnct_inv_global
            fnct_inv=_function_field_fnct_inv_method,
            fnct_inv_arg=None,
            # type is the field type name returned by the function. It can be any field type name except function.
            type='many2one',
            obj='tr.demo.a',
            # relation="",
            # fnct_search allows you to define the searching behaviour on that field.
            fnct_search=None,
            # method whether the field is computed by a method (of an object) or a global function
            method=True,
            # store If you want to store field in database or not. Default is False.
            # It will call function function_name when any changes are written to fields
            # in the list ['field1','field2'] on object 'object_name'.
            store={
                'hr.demo.b': (
                    #function_name,
                    _function_field_store_method,
                    ['a_id', ],
                    # priority
                    10
                )
            },
            # multi is a group name. All fields with the same multi parameter will be calculated in a single function call.
            multi=False,
            # TODO
            arg=None,
            string='Function',
        ),

    }

    _defaults = {
    }


class DemoB(osv.osv):
    _name = 'tr.demo.b'

    _columns = {
        'many2many_field': fields.many2many('tr.demo.a', 'tr_demo_a_b', 'b_id', 'a_id', 'Many2Many A demos'),
        'a_id': fields.many2one('tr.demo.a', 'Demo A'),
    }

    _defaults = {
    }