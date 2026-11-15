const $ = id => document.getElementById(id);
const node = (tag, text, cls) => { const e = document.createElement(tag); if (text !== undefined) e.textContent = text; if (cls) e.className = cls; return e; };
$('form').addEventListener('submit', async e => {
 e.preventDefault(); $('submit').disabled = true;
 try {
  const response = await fetch('/api/answer', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({situation:$('situation').value,official_text:$('official').value,source_url:$('url').value})});
  if (!response.ok) throw new Error('The request could not be processed.');
  const data = await response.json(); $('empty').hidden=true; $('results').hidden=false; $('warning').textContent=data.warning; $('missing').textContent=data.missing;
  $('sources').replaceChildren(); $('checklist').replaceChildren(); $('fields').replaceChildren(); $('material').replaceChildren();
  if (!data.sources.length) $('sources').append(node('p','No matching evidence found. Contact your university international office or the relevant authority.'));
  data.sources.forEach(s => {const box=node('article',undefined,'source'); box.append(node('div',`[${s.id}] ${s.topic.toUpperCase()}`,'tag'),node('p',`“${s.quote}” [${s.id}]`)); const a=node('a',s.title); a.href=s.url; a.target='_blank'; a.rel='noopener noreferrer'; box.append(a,node('small',`${s.publisher} · ${s.country} · checked ${s.date} · demo paraphrase, not a verbatim quotation`)); $('sources').append(box);});
  data.checklist.forEach(t=>{const row=node('div',undefined,'task'); const check=node('input'); check.type='checkbox'; row.append(check,document.createTextNode(` ${t.date} · ${t.action} [${t.source}]`)); $('checklist').append(row)});
  if (!data.fields.length) $('fields').append(node('p','No form fields identified for the matched sources.'));
  data.fields.forEach(f=>{const wrap=node('label',undefined,'field'); wrap.append(document.createTextNode(`${f.label} [${f.source}]`)); const input=node('input'); input.value=f.value; input.placeholder='Needs your review'; wrap.append(input); const a=node('a','View source form'); a.href=f.form_url; a.target='_blank'; a.rel='noopener noreferrer'; wrap.append(a); $('fields').append(wrap)});
  if(data.user_material){$('material').append(node('h3','Your unverified material'),node('p',data.user_material.text || 'No text provided.'),node('p',data.user_material.url || 'No URL provided.'));}
 } catch(err){alert(err.message)} finally{$('submit').disabled=false}
});
