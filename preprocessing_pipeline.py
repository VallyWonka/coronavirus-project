#!/usr/bin/python
# -*- coding: UTF-8 -*-

from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    Doc
)


SEGMENTER = Segmenter()
EMBEDDINGS = NewsEmbedding()
MORPH_TAGGER = NewsMorphTagger(EMBEDDINGS)
MORPH_VOCAB = MorphVocab()

POS_TAGS = ["ADJ", "ADV", "VERB", "NOUN", "PROPN"]


def tokenize(doc: Doc, segmenter: Segmenter):
    doc.segment(segmenter)


def morph_tag(doc: Doc, tagger: NewsMorphTagger):
    doc.tag_morph(tagger)


def filter(doc: Doc):
    return [token for token in doc.tokens if token.pos in POS_TAGS]


def lemmatize(doc: list, vocab: MorphVocab):
    lemmatized = []
    for token in doc:
        token.lemmatize(vocab)
        lemmatized.append(token.lemma)
    return lemmatized


def preprocess(text: str):
    doc = Doc(text)
    tokenize(doc, SEGMENTER)
    morph_tag(doc, MORPH_TAGGER)
    doc = lemmatize(filter(doc), MORPH_VOCAB)
    return " ".join(doc)
