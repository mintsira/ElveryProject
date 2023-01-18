
from DBHelper import DBHelper

class ReportUnpaidInvoices:
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

    print ("Report unpaid invoices")
    db = DBHelper()
    data, columns = db.fetch (
                            'SELECT "Invoice No", i.date as "Invoice Date", \
		                        c.name as "Customer Name", i.amount_due as "Invoice Amount Due",\
		                        "Invoice Amount Received", i.amount_due - "Invoice Amount Received" as "Invoice Amount Not piad"\
                            FROM(SELECT rli.invoice_no AS "Invoice No", SUM(rli.amount_paid_here) as "Invoice Amount Received"\
	                            FROM receipt_line_item as rli \
	                            GROUP BY rli.invoice_no ) as li \
                            JOIN invoice as i \
	                            ON li."Invoice No" = i.invoice_no \
                            JOIN customer as c \
	                            ON i.customer_code = c.customer_code \
                            WHERE i.amount_due - "Invoice Amount Received" !=  0'
                            )
    data1, columns1 = db.fetch (
                            'SELECT SUM(i.amount_due - "Invoice Amount Received") AS "Total invoice amount not paid", COUNT(li) AS "Number of Invoice not paid" \
                            FROM(SELECT rli.invoice_no AS "Invoice No", SUM(rli.amount_paid_here) as "Invoice Amount Received"\
	                            FROM receipt_line_item as rli\
	                            GROUP BY rli.invoice_no )as li\
                            INNER JOIN invoice as i\
	                            ON li."Invoice No" = i.invoice_no')
                                
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