"""
* 'request nms sdavc status'
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# ===========================================
# Schema for 'request nms sdavc status'
# ===========================================

class RequestNmsSdavcStatusSchema(MetaParser):
    """Schema for "request nms sdavc status" """

    schema = {
        "Enabled": str,
        "Status": str,
    }


# ===========================================
# Parser for 'show system status'
# ===========================================


class RequestNmsSdavcStatus(RequestNmsSdavcStatusSchema):
    """Parser for "request nms sdavc status" """

    cli_command = "request nms sdavc status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        #         Enabled: false
        p1 = re.compile(r"^\s*(?P<type>.*):\s(?P<value>.*)$")

        #         Status: not running
        # p2 = re.compile(r"^\s*Status: (.*)$")

        for line in output.splitlines():
            line = line.strip()

            # System logging to host is disabled
            # System logging to disk is enabled
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                parsed_dict[group["type"]] = group["value"]

        return parsed_dict
