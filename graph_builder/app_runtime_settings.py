import sys


class AppRuntimeSettings(object):
    options_to_alias_config = {
        'input': 'i',
        'output': 'o',
        'verbose': 'v'
    }

    options_value_mapper = {
        'input': 'test.osm.pbf',
        'output': 'result.json',
        'verbose': False
    }

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            original_instance = super(AppRuntimeSettings, cls)
            cls._instance = original_instance.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        for argument in sys.argv:
            # TODO показывать ошибку если передан невалидный аргумент
            for option_name, alias in self.options_to_alias_config.items():
                is_option_without_value = argument == f'--{option_name}' or argument == f'-{alias}'
                is_option_has_value = argument.startswith(f'--{option_name}=') or argument.startswith(f'-{alias}=')

                if is_option_has_value:
                    if argument.startswith(f'--{option_name}='):
                        self.options_value_mapper[option_name] = argument.replace(f'--{option_name}=', '')

                    if argument.startswith(f'-{alias}='):
                        self.options_value_mapper[option_name] = argument.replace(f'-{alias}=', '')
                elif is_option_without_value:
                    self.options_value_mapper[option_name] = True

    @property
    def input_filepath(self):
        return self.options_value_mapper['input']

    @property
    def graph_output_filepath(self):
        return self.options_value_mapper['output']

    @property
    def is_verbose_logging_enabled(self):
        return self.options_value_mapper['verbose']
