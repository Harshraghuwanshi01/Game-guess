from sql_connection import get_sql_connection 
def get_all_products(connection):#worked properly
    cursor=connection.cursor()
    query="SELECT products.product_id,products.name,products.uom_id,products.price_per_unit,uom.uom_name FROM gs.products inner join gs.uom on products.uom_id=uom.uom_id"
    cursor.execute(query)
    response=[]
    for (product_id,name,uom_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'name':name,
                'uom_id':uom_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }
        )
    connection.close()
    return response


def insert_new_Product(connection,product):#insert function is not working 
    cursor=connection.cursor()
    query=("insert into products (product_id,name,uom_id,price_Per_unit) values (%s,%s,%s,%s)")
    data=(product['product_id'],product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid



def delete_product(connection,product_id):#worked properly
    cursor=connection.cursor()
    query=("DELETE FROM products where product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()
if __name__=='__main__':
    connection=get_sql_connection()
    print(get_all_products(connection))