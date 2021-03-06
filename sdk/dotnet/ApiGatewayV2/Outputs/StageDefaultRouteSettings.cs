// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.ApiGatewayV2.Outputs
{

    [OutputType]
    public sealed class StageDefaultRouteSettings
    {
        /// <summary>
        /// Whether data trace logging is enabled for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
        /// Defaults to `false`. Supported only for WebSocket APIs.
        /// </summary>
        public readonly bool? DataTraceEnabled;
        /// <summary>
        /// Whether detailed metrics are enabled for the default route. Defaults to `false`.
        /// </summary>
        public readonly bool? DetailedMetricsEnabled;
        /// <summary>
        /// The logging level for the default route. Affects the log entries pushed to Amazon CloudWatch Logs.
        /// Valid values: `ERROR`, `INFO`, `OFF`. Defaults to `OFF`. Supported only for WebSocket APIs.
        /// </summary>
        public readonly string? LoggingLevel;
        /// <summary>
        /// The throttling burst limit for the default route.
        /// </summary>
        public readonly int? ThrottlingBurstLimit;
        /// <summary>
        /// The throttling rate limit for the default route.
        /// </summary>
        public readonly double? ThrottlingRateLimit;

        [OutputConstructor]
        private StageDefaultRouteSettings(
            bool? dataTraceEnabled,

            bool? detailedMetricsEnabled,

            string? loggingLevel,

            int? throttlingBurstLimit,

            double? throttlingRateLimit)
        {
            DataTraceEnabled = dataTraceEnabled;
            DetailedMetricsEnabled = detailedMetricsEnabled;
            LoggingLevel = loggingLevel;
            ThrottlingBurstLimit = throttlingBurstLimit;
            ThrottlingRateLimit = throttlingRateLimit;
        }
    }
}
