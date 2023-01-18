
from DBHelper import DBHelper

class ReportListAllReceipts:
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

    print ("Report list all receipts")
    db = DBHelper()
    data,columns = db.fetch('select receipt.receipt_no from receipt; ')
    for A in data:
        print("\n")
        db = DBHelper()
        data,columns = db.fetch( 'SELECT r.receipt_no as "Receipt No", '
        '   r.date as "Receipt Date", '
        '   r.customer_code as "Customer Code", '
         '  c.name as "Customer Name" , '
         '   pm.description as "Payment Name", '
        '	r.total_received as "Total Received", '
          'r.payment_reference as "Payment Reference", '
       '	r.remarks as "Remarks" ' 
        'FROM receipt r '
        ' JOIN customer c ON c.customer_code = r.customer_code '
         'JoIn payment_method  pm on pm.payment_method = r.payment_method '
         " where r.receipt_no='{}' ".format(A[0]))


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