from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator
from models.history_model import HistoryModel

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def get_translate():
    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate="O que deseja traduzir?",
        translate_from="pt",
        translate_to="en",
        translated="What do you want to translate?"
    )


@translate_controller.route("/", methods=["POST"])
def post_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    data_history = {
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
    }
    HistoryModel(data_history).save()

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated
    )


@translate_controller.route("/reverse", methods=["POST"])
def reverse_translate():
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate
    )
