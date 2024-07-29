from odoo import tools

from odoo.tools.translate import TranslationImporter
from odoo.modules import get_resource_path
from . import models


def _override_translation_term(env):
    module_name = 'viin_brand_pos'
    translation_importer = TranslationImporter(env.cr)
    for lang, _ in env['res.lang'].get_installed():
        lang_code = tools.get_iso_codes(lang)
        # Step 1: reset translation terms with base language file
        if '_' in lang_code:
            base_lang_code = lang_code.split('_')[0]
            base_trans_file = get_resource_path(module_name, 'i18n_extra', base_lang_code + '.po')
            if base_trans_file:
                translation_importer.load_file(base_trans_file, lang)
        # Step 2: reset translation file with main language file (can possibly override the
        # terms coming from the base language)
        trans_file = get_resource_path(module_name, 'i18n_extra', lang_code + '.po')
        if trans_file:
            translation_importer.load_file(trans_file, lang)
    translation_importer.save(overwrite=True)


def post_init_hook(env):
    _override_translation_term(env)