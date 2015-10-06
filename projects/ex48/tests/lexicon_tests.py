from nose.tools import *
from InputScanner import lexicon


def test_directions():
    assert_equal(lexicon.scan("north"), [('directions', 'north')])
    result = lexicon.scan("north SOUTH east")
    assert_equals(result, [('directions', 'north'),
                           ('directions', 'south'),
                           ('directions', 'east')])


def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in off")
    assert_equal(result, [('stop', 'the'), ('stop', 'in'), ('stop', 'off')])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'), ('noun', 'princess')])


def test_numbers():
    assert_equal(lexicon.scan("2"), [('number', 2)])
    result = lexicon.scan("123 64848 8989")
    assert_equal(result, [('number', 123), ('number', 64848), ('number', 8989)])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'asdfadfasdf')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'ias'),
                          ('noun', 'princess')])