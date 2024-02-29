from app import AbcApplication

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    if len(args) == 0:
        app = AbcApplication(mode='client')
    elif len(args) == 1:
        if args[0].lower() == 'server':
            app = AbcApplication(mode='server')
        else:
            app = AbcApplication(host=args[0])
    elif len(args) == 2:
        if args[0].lower() == 'server':
            app = AbcApplication(mode='server', host=args[1])
        else:
            print("Invalid arguments")
            sys.exit(1)
    else:
        print("Invalid arguments")
        sys.exit(1)
    app.start()