const std = @import("std"); //std library import

pub fn main() void {
    std.debug.print("Hello, {s}!\n", .{"World"});
}
