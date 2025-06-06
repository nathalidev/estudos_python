frappe.ui.form.on('NomeDoDocType', {
  before_submit(frm) {
    console.log("before_submit acionado");
  },
  on_submit(frm) {
    console.log("on_submit acionado");
  },
  before_cancel(frm) {
    console.log("before_cancel acionado");
  },
  after_cancel(frm) {
    console.log("after_cancel acionado");
  },
  before_discard(frm) {
    console.log("before_discard acionado");
  },
  after_discard(frm) {
    console.log("after_discard acionado");
  },
  timeline_refresh(frm) {
    console.log("timeline_refresh acionado");
  },
  minha_tabela_on_form_rendered(frm, cdt, cdn) {
    console.log("Linha da tabela renderizada");
  },
  meu_campo(frm) {
    console.log("Campo meu_campo foi alterado");
  },
  get_email_recipient_filters(frm, field) {
    return {
      "email_group": ["=", "Clientes"]
    };
  },
  get_email_recipients(frm, field) {
    return ["cliente@exemplo.com", "suporte@exemplo.com"];
  }
});


