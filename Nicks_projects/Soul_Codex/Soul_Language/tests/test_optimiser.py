from src.sqly.parser import Phrase, Query
from src.sqly.optimiser import optimise
from src.sqly.lowering import lower
from src.ntru import generate_keypair


def test_phrase_merge_single_frame():
    ast = Query([Phrase("foo"), Phrase("foo"), Phrase("foo")])
    opt = optimise(ast)
    assert len(opt.phrases) == 1
    assert opt.phrases[0].merged is True

    frames = lower(ast, "intent", generate_keypair())
    assert sum(1 for f in frames if f.ttt == 1) == 1


def test_phrase_not_merge_different_text():
    ast = Query([Phrase("foo"), Phrase("bar")])
    opt = optimise(ast)
    assert len(opt.phrases) == 2

    frames = lower(ast, "intent", generate_keypair())
    assert sum(1 for f in frames if f.ttt == 1) == 2
