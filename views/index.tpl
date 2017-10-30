%rebase('base.tpl', page_title="People List")
<h3>People</h3>
<ul>
%for row in rows:
    %if not str(row[1]):
        %var = "[!]-NULL"

    %else:
        %id = row[0]
        %name = row[1]
    %end
<li><a href="/item{{row[0]}}">{{id}} - {{name}}</a></li>
%end
</ul>
<br>
<form>
<input type="button" name="" value="Add New Register" onclick="parent.location='/new'">
</form>
