from invoke import Collection

from . import (
    build,
    database,
    lint,
    test,
)

ns = Collection()
# Top level tasks
ns.add_task(build.dist, name="build")
ns.add_task(build.requirements)
ns.add_task(build.release)
ns.add_task(database.local_db)
ns.add_task(database.local_db_stop)
ns.add_task(test.test)
# Module collection tasks
ns.add_collection(lint)
