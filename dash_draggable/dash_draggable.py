# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class dash_draggable(Component):
    """A dash_draggable component.
...

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): ...
- id (string; optional): The ID used to identify this component in Dash callbacks
- axis (string; optional): ...
- handle (string; optional): ...
- defaultPosition (dict; optional): ...
- getPosition (dict; optional): ...
- getEvent (dict; optional): ...
- position (dict; optional): ...
- grid (list; optional): ...
- disabled (boolean; optional): ..."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, onDrag=Component.UNDEFINED, axis=Component.UNDEFINED, handle=Component.UNDEFINED, defaultPosition=Component.UNDEFINED, getPosition=Component.UNDEFINED, getEvent=Component.UNDEFINED, position=Component.UNDEFINED, grid=Component.UNDEFINED, disabled=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'axis', 'handle', 'defaultPosition', 'getPosition', 'getEvent', 'position', 'grid', 'disabled']
        self._type = 'dash_draggable'
        self._namespace = 'dash_draggable'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'axis', 'handle', 'defaultPosition', 'getPosition', 'getEvent', 'position', 'grid', 'disabled']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(dash_draggable, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('dash_draggable(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'dash_draggable(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
