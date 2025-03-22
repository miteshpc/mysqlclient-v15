from frappe import database

__version__ = "0.0.1"


def get_db(
    host=None, user=None, password=None, port=None, cur_db_name=None, socket=None
):
    import frappe

    conf = frappe.local.conf

    if conf.db_type == "postgres":
        import frappe.database.postgres.database

        return frappe.database.postgres.database.PostgresDatabase(
            host, user, password, port, cur_db_name, socket
        )

    elif conf.use_mysqlclient:
        from mysqlclient_v15.mysqlclient import MariaDBDatabase

        return MariaDBDatabase(host, user, password, port, cur_db_name, socket)

    else:
        import frappe.database.mariadb.database

        return frappe.database.mariadb.database.MariaDBDatabase(
            host, user, password, port, cur_db_name, socket
        )


database.get_db = get_db
