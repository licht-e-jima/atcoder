from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ClosedTime:
    """標準ライブラリの datetime.time が 24:00 に対応していないため、独自に実装する
    """
    start_h: int
    start_m: int
    end_h: int
    end_m: int

    def __post_init__(self):
        assert (
            0 <= self.start_h <= 23 and
            0 <= self.end_h <= 24 and
            0 <= self.start_m <= 60 and
            0 <= self.end_m <= 60 and
            (
                self.start_h < self.end_h or
                (
                    self.start_h == self.end_h and
                    self.start_m < self.end_m
                )
            )
        ), f"START: {self.start_h}:{self.start_m}\tEND: {self.end_h}:{self.end_m}"

    @classmethod
    def from_str(cls, time_span_str: str) -> "ClosedTime":
        start_time, end_time = time_span_str.split("-")
        start_h = int(start_time[:2])
        start_m = int(start_time[3:])
        end_h = int(end_time[:2])
        end_m = int(end_time[3:])
        return cls(start_h, start_m, end_h, end_m)

    def is_within_closing_time(self, t: datetime) -> bool:
        if self.start_h == self.end_h:
            return (
                self.start_h == t.hour and
                self.start_m <= t.minute < self.end_m
            )
        else:
            return (
                (
                    self.start_h == t.hour and
                    self.start_m <= t.minute
                ) or
                self.start_h < t.hour < self.end_h or
                (
                    t.hour == self.end_h and
                    t.minute < self.end_m
                )
            )
