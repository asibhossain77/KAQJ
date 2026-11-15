from kaqj.main import main


def test_main(capsys):
    main()

    captured = capsys.readouterr()

    assert "KAQJ AI" in captured.out
    assert "Your local AI assistant is getting ready!" in captured.out