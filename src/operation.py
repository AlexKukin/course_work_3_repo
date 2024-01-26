from datetime import date


class Operation:
    def __init__(self, _id, _date, description, send_from, send_to, amount, name):
        self.id = _id
        self.date = _date
        self.description = description
        self.send_from = send_from
        self.send_to = send_to
        self.amount = amount
        self.name = name

    def __repr__(self):
        return (f"Operation(_id={self.id}, _date={self.date}, description={self.description},\n"
                f"send_from={self.send_from}, send_to={self.send_to},\n"
                f"amount={self.amount}, name={self.name})\n")

    def __str__(self):
        return (f"{self.date} {self.description}\n"
                f"{self.send_from} -> {self.send_to}\n"
                f"{self.amount} {self.name}\n")

    def hide_info_send_from(self):
        self.send_from = self.hide_bill_info(self.send_from)

    def hide_info_send_to(self):
        self.send_to = self.hide_bill_info(self.send_to)

    def format_date(self):
        """"""
        format_data = date.fromisoformat(self.date[:10])
        self.date = format_data.strftime("%d.%m.%Y")
        return self.date

    def depersonalize(self):
        self.hide_info_send_from()
        self.hide_info_send_to()
        self.format_date()

    @staticmethod
    def hide_bill_info(bill):
        if bill == '':
            return bill

        if bill.startswith('Счет'):
            bill = f"{bill[0:4]} **{bill[-4:]}"
        else:
            bill = f"{bill[0:-12]} {bill[-12:-10]}** **** {bill[-4:]}"
        return bill
