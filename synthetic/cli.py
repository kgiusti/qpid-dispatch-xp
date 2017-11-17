#!/usr/bin/env python
import click
import logging
import tasks as t

logging.basicConfig(level=logging.DEBUG)

## cli part
@click.group()
def cli():
    pass


@cli.command()
@click.argument('broker')
@click.option("--provider",
    default="vagrant",
    help="Deploy with the given provider")
@click.option("--force",
    is_flag=True)
def deploy(broker, provider, force):
    providers = {
        "g5k": t.g5k,
        "vagrant": t.vagrant
    }
    p = providers[provider]

    p(broker=broker, force=force)
    t.inventory()
    t.prepare(broker=broker)


@cli.command()
@click.option("--force", is_flag=True, help="force redeploy")
def g5k(force):
    t.g5k(force)


@cli.command()
@click.option("--force",is_flag=True, help="force redeploy")
def vagrant(force):
    t.vagrant(force)


@cli.command()
def inventory():
    t.inventory()


@cli.command()
def prepare():
    t.prepare()


@cli.command(help="""
    Runs the test case 1 : one single large (distributed) target.

    Workflow:

        ./cli.py test_case_1 --nbr_clients 10 --nbr_servers 2

        ./cli.py destroy

        ./cli.py test_case_1 --nbr_clients 20 --nbr_servers 2
""")
@click.option("--nbr_clients",
    default="1",
    help="Number of clients that will de deployed")
@click.option("--nbr_servers",
    default="1",
    help="Number of servers that will de deployed")
@click.option("--call_type",
    default="rpc-call",
    type=click.Choice(["rpc-call", "rpc-cast", "rpc-fanout"]),
    help="Rpc_call (blocking) or rpc_cast (non blocking) [client] ")
@click.option("--nbr_calls",
    default="100",
    help="Number of calls/cast to execute [client]")
@click.option("--pause",
    default=0.0,
    help="Pause in second between each call [client]")
@click.option("--timeout",
    default=60,
    help="Total time in second of the benchmark [controller]")
@click.option("--version",
    default="latest",
    help="Version of ombt to use as a docker tag (will use beyondtheclouds:'vesion')")
@click.option("--verbose",
    is_flag=True,
    help="Verbose mode will log every single message stat [client|server]")
def test_case_1(nbr_clients, nbr_servers, call_type, nbr_calls, pause, timeout, version, verbose):
    t.test_case_1(nbr_clients, nbr_servers, call_type,
                  nbr_calls, pause, timeout, version, verbose=verbose)

@cli.command()
def destroy():
    t.destroy()

@cli.command()
def backup():
    t.backup()


if __name__ == "__main__":
    cli()
