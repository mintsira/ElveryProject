
from DBHelper import DBHelper

class MainDishes:
    pass

def Report():
    print ("""<html>
                <head>
                    <title>Report Invoice</title>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <link rel='stylesheet' href='//cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css'>
                    <script src='//cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js'></script>
                    <script src="static/cpe.js"></script>
                    <link rel='stylesheet' href='static/cpe.css'>
                </head>
                <body><h1>Report Invoice.</h1>
                <ul class="nav">
                    <li><a href="index.html">Main</a></li>
                    <li><a href="ReportListAllInvoices">Report list all invoices</a></li>
                    <li><a href="ReportProductsSold">Report products sold</a></li>
                    <li><a href="ReportListAllProducts">Report list all products</a></li>
                    <li><a href="ReportListAllReceipts">Report list all receipts</a></li>
                    <li><a href="ReportUnpaidInvoices">Report unpaid invoices</a></li>
                    <li><a href="ReportProductsSoldTotal">Report products sold total </a></li>
                </ul>
                <div id='div-lab3'></div>
                """)

    print ("Report list all invoices")
    db = DBHelper()
    data, columns = db.fetch ('SELECT i.invoice_no as "Invoice No", i.date as "Date" '
                            ' , i.customer_code as "Customer Code", c.name as "Customer Name" '
                            ' , i.due_date as "Due Date", i.total as "Total", i.vat as "VAT", i.amount_due as "Amount Due" '
                            ' , ili.product_code as "Product Code", p.name as "Product Name" '
                            ' , ili.quantity as "Quantity", ili.unit_price as "Unit Price", ili.product_total as "Extended Price" '
                            ' FROM invoice i JOIN customer c ON i.customer_code = c.customer_code '
                            '  JOIN invoice_line_item ili ON i.invoice_no = ili.invoice_no '
                            '  JOIN product p ON ili.product_code = p.code '
                            ' ')
    print ("<table id='maintable' class='display table-lab3'>")
    print ("<tr>")
    for col in columns: 
        print ("<th>" + col + "</th>")
    print ("</tr>")
    
    for row in data: 
        print ("<tr>")
        for col in row:
            print ("<td>" + str(col) + "</td>")
        print ("</tr>")
    print ("</table>")
    print ("</body></html>")