from PyQt5 import QtWidgets


def populate_fields(window, gui_data):
    """
    Function to populate with data and options the different fields in the GUI

    Parameters
    window (PetaloRunConfigurationGUI): Main application
    gui_data (dictionary): Dictionary with the different fields values and defaults
        The structure is the one in gui/widget_data.py
    """
    for field, entries in gui_data.items():
        widget = getattr(window, field)
        # Add all items in the case of QComboBox
        if isinstance(widget, QtWidgets.QComboBox):
            for index, item in entries['values'].items():
                widget.addItem(item['text'], item['value'])

        # Set default value for different widget types
        if isinstance(widget, QtWidgets.QComboBox):
            widget.setCurrentIndex(entries['default'])
        if isinstance(widget, QtWidgets.QCheckBox):
            widget.setChecked(entries['default'])
        if isinstance(widget, QtWidgets.QSpinBox):
            widget.setValue     (entries['default'])
            if 'min' in entries:
                widget.setMinimum   (entries['min'])
            if 'max' in entries:
                widget.setMaximum   (entries['max'])
            if 'step' in entries:
                widget.setSingleStep(entries['step'])
        if isinstance(widget, QtWidgets.QDoubleSpinBox):
            widget.setValue     (entries['default'])
            if 'min' in entries:
                widget.setMinimum   (entries['min'])
            if 'max' in entries:
                widget.setMaximum   (entries['max'])
            if 'step' in entries:
                widget.setSingleStep(entries['step'])
            if 'decimals' in entries:
                widget.setSingleStep(entries['decimals'])


def read_parameters(window, fields_data, params_tuple):
    """
    Function to read a set of field values from the GUI and store them in
    a named tuple. The names in the GUI (field_data) must follow the pattern
    {widgetType}_{name} such as comboBox_e_hysteresis. The names in params_tuple
    will be the same removing the first word before "_".


    Parameters
    window (QApplication): Parent window
    fields_data (dictionary): TODO
    parameters (namedtuple creator): NamedTuple creator with a matching
        structure for fields_data. Samples in gui/types.py

    Returns:
    namedtuple: Filled with the corresponding values for each parameter
    """
    params = {}

    for field, values in fields_data.items():
        fieldname = '_'.join(field.split('_')[1:])

        widget = getattr(window, field)
        if isinstance(widget, QtWidgets.QComboBox):
            params[fieldname] = widget.currentData()
        if isinstance(widget, QtWidgets.QCheckBox):
            status = widget.isChecked()
            params[fieldname] = fields_data[field]['values'][status]['value']
        if isinstance(widget, QtWidgets.QSpinBox):
            params[fieldname] = widget.value()
        if isinstance(widget, QtWidgets.QDoubleSpinBox):
            params[fieldname] = int(widget.value())

    parameters = params_tuple(**params)

    return parameters
