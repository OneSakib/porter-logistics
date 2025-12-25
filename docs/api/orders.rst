.. _orders_api:

=====================
Order Management
=====================

The NimbusPost provides APIs to create, retrieve, cancel, and manage customer
orders from your workspace. This page explains all order-related operations with
complete examples.

Before using the orders API, ensure the SDK is initialized with valid
credentials.

------------------------
Basic Usage Example
------------------------

Below is a complete working script demonstrating all available order
operations via the NimbusPost.

.. code-block:: python

    """
    Example: Setup order using NimbusPost
    """

    from nimbuspost import NimbusPost
    import os
    from dotenv import load_dotenv
    load_dotenv()


    

    def main():
        sdk = NimbusPost(
            workspace=os.getenv('ESHOPBOX_WORKSPACE', ''),
            client_id=os.getenv('ESHOPBOX_CLIENT_ID', ''),
            client_secret=os.getenv('ESHOPBOX_SECRET_ID', ''),
            refresh_token=os.getenv('ESHOPBOX_REFRESH_TOKEN', '')
        )

    if __name__ == "__main__":
        main()

------------------------
API Reference
------------------------

Get All Orders
==============

**Method**

``sdk.orders.get_all(page: int = 1, **filters)``

**Description**

Fetch a paginated list of orders.

**Example**

.. code-block:: python

    orders = sdk.orders.get_all(page=1, filters="account=<account-name>")
    print(orders)


Get Single Order
================

**Method**

``sdk.orders.get(order_id: str)``

**Example**

.. code-block:: python

    order = sdk.orders.get("OD119208447831346001")
    print(order)


Create Order
============

**Method**

``sdk.orders.create(order_payload: dict)``

Full payload example is included above.

**Example**

.. code-block:: python

    response = sdk.orders.create(order)
    print(response)


Cancel Order
============

**Method**

``sdk.orders.cancel(cancel_payload: dict)``

**Example**

.. code-block:: python

    response = sdk.orders.cancel(cancel_data)
    print(response)


Get Invoice
===========

**Method**

``sdk.orders.get_invoice(order_id: str)``

**Example**

.. code-block:: python

    invoice = sdk.orders.get_invoice("OD119208447831346002")
    print(invoice)

------------------------
Environment Variables
------------------------

Store credentials in a `.env` file:

.. code-block:: bash

    ESHOPBOX_WORKSPACE="your-workspace"
    ESHOPBOX_CLIENT_ID="your-client-id"
    ESHOPBOX_SECRET_ID="your-secret-id"
    ESHOPBOX_REFRESH_TOKEN="your-refresh-token"
    ESHOPBOX_EXTERNAL_CHANNEL_ID="your-channel-id"

------------------------
Next Steps
------------------------

- See :ref:`inventory_api` to manage stock levels.
- See :ref:`products_api` to manage your catalog.
